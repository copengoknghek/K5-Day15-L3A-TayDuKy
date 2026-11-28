const LABELS = { answer: "Trả lời", ask_back: "Hỏi lại", not_found: "Không có trong tài liệu", refuse: "Từ chối" };
const HAS_LAB = /(day|lab|ng[aà]y)\s*0*\d+/i;
const STORE = "tayduky-chats";  // lịch sử chỉ nằm trong trình duyệt này
const KEEP = 20;                // số cuộc trò chuyện giữ lại
let labs = [];
let chosen = "";       // "" = chưa chọn lab
let current = null;    // cuộc trò chuyện đang mở; null = chưa hỏi gì
let chats = load();

function load() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORE));
    return Array.isArray(saved) ? saved.filter((c) => c && Array.isArray(c.items)) : [];
  } catch {
    return [];  // trình duyệt chặn lưu trữ thì vẫn chat được, chỉ không giữ lịch sử
  }
}

function save() {
  try {
    localStorage.setItem(STORE, JSON.stringify(chats.slice(0, KEEP)));
  } catch { /* không lưu được thì thôi */ }
}

// Trích dẫn "[repo/file.md#mục]" → link tới đúng file ở commit đã ghim; `chữ` → <code>.
function inline(line) {
  const parts = [];
  const pattern = /\[([^\[\]\n]+?\.md#(?:[^\[\]\n]|\[[^\]\n]*\])+)\]|`([^`\n]+)`|\*\*([^*\n]+)\*\*/g;
  let last = 0;
  for (const m of line.matchAll(pattern)) {
    parts.push(line.slice(last, m.index));
    if (m[1]) parts.push(citation(m[1]));
    else if (m[2]) parts.push(el("code", { textContent: m[2] }));
    else parts.push(el("strong", { textContent: m[3] }));
    last = m.index + m[0].length;
  }
  parts.push(line.slice(last));
  return parts;
}

function citation(code) {
  const [path, ...rest] = code.split("#");
  const [repo, ...file] = path.split("/");
  const lab = labs.find((l) => l.repo === repo);
  const label = (lab ? lab.label + " · " : "") + file.join("/") + " › " + rest.join("#");
  if (!lab) return el("span", { className: "cite", textContent: label });
  const href = lab.url.replace("/tree/", "/blob/") + "/" + file.map(encodeURIComponent).join("/");
  return el("a", { className: "cite", href, target: "_blank", rel: "noopener noreferrer", textContent: label });
}

function scrollDown() {
  $("messages").scrollTop = $("messages").scrollHeight;
}

function personIcon() {
  const svg = "http://www.w3.org/2000/svg";
  const icon = document.createElementNS(svg, "svg");
  icon.setAttribute("viewBox", "0 0 24 24");
  icon.setAttribute("aria-hidden", "true");
  const path = document.createElementNS(svg, "path");
  path.setAttribute("d", "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8ZM4.5 20a7.5 7.5 0 0 1 15 0");
  icon.append(path);
  return icon;
}

// Mỗi tin nhắn là một hàng: ảnh đại diện + bong bóng. Trả về bong bóng.
function add(bubble) {
  const mine = bubble.classList.contains("user");
  const avatar = mine
    ? el("span", { className: "avatar person", title: "Bạn" }, personIcon())
    : el("img", { className: "avatar", src: "/bot.png", alt: "Bot" });
  $("welcome").hidden = true;
  $("messages").append(el("div", { className: mine ? "row user" : "row bot-row" }, avatar, bubble));
  scrollDown();
  return bubble;
}

function fill(bubble, kind, label, text) {
  const badge = el("span", { className: "badge", textContent: label });
  badge.dataset.kind = kind;
  bubble.replaceChildren(badge, ...text.split("\n").filter((l) => l.trim()).map((l) => el("p", {}, ...inline(l))));
  scrollDown();
}

function show(chat) {
  current = chat;
  for (const node of $("messages").querySelectorAll(".row")) node.remove();
  $("welcome").hidden = Boolean(chat);
  for (const item of chat ? chat.items : []) {
    if (item.mine) add(el("div", { className: "msg user", textContent: item.text }));
    else fill(add(el("div", { className: "msg bot-msg" })), item.kind, item.label, item.text);
  }
  drawHistory();
}

function drawHistory() {
  $("history-empty").hidden = chats.length > 0;
  $("wipe").hidden = chats.length === 0;
  $("history").replaceChildren(...chats.map((chat) => {
    const open = el("button", { type: "button", className: "open", textContent: chat.title, title: chat.title });
    if (chat === current) open.setAttribute("aria-current", "true");
    open.addEventListener("click", () => { if (!$("send").disabled) show(chat); });
    const remove = el("button", { type: "button", className: "remove", textContent: "×", ariaLabel: `Xoá: ${chat.title}` });
    remove.addEventListener("click", () => {
      if ($("send").disabled) return;
      chats = chats.filter((c) => c !== chat);
      save();
      show(chat === current ? null : current);
    });
    return el("li", {}, open, remove);
  }));
}

async function ask(raw) {
  // đã chọn lab mà câu hỏi không nêu lab thì gắn vào đầu, và hiện đúng câu đã gửi
  const question = chosen && !HAS_LAB.test(raw) ? `Lab ${chosen}: ${raw}` : raw;
  const chat = current || { title: question, lab: null, items: [] };  // lab: chỉ nhớ số lab, không nhớ nội dung
  if (!current) chats = [chat, ...chats].slice(0, KEEP);
  current = chat;
  chat.items.push({ mine: true, text: question });
  save();
  drawHistory();
  add(el("div", { className: "msg user", textContent: question }));
  const bubble = add(el("div", { className: "msg bot-msg" }, el("span", { className: "typing", textContent: "Đang tra tài liệu…" })));
  $("send").disabled = true;
  let reply;
  try {
    const response = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, lab: chat.lab }),
    });
    const data = await response.json();
    if (!response.ok) reply = { kind: "error", label: "Chưa trả lời được", text: data.error };
    else {
      chat.lab = data.lab;
      reply = { kind: data.decision || "", label: LABELS[data.decision] || "Kết quả", text: data.text };
    }
  } catch {
    reply = { kind: "error", label: "Chưa trả lời được", text: "Không kết nối được máy chủ." };
  }
  fill(bubble, reply.kind, reply.label, reply.text);
  chat.items.push(reply);
  save();
  $("send").disabled = false;
}

$("form").addEventListener("submit", (event) => {
  event.preventDefault();
  const raw = $("question").value.trim();
  if (!raw || $("send").disabled) return;
  $("question").value = "";
  ask(raw);
});

$("question").addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey && !event.isComposing) {
    event.preventDefault();
    $("form").requestSubmit();
  }
});

for (const button of document.querySelectorAll(".samples button")) {
  button.addEventListener("click", () => { if (!$("send").disabled) ask(button.textContent); });
}

$("new-chat").addEventListener("click", () => {
  if (!$("send").disabled) show(null);
});

$("wipe").addEventListener("click", () => {
  if ($("send").disabled || !confirm("Xoá toàn bộ lịch sử trò chuyện trên trình duyệt này?")) return;
  chats = [];
  save();
  show(null);
});

drawHistory();

stats.then((data) => {
  labs = data.labs;
  if (current) show(current);  // vẽ lại để trích dẫn thành link khi đã có danh sách lab
  const options = [["", "Chưa chọn lab"], ...labs.map((l) => [l.label, l.label])];
  $("picker").replaceChildren(...options.map(([value, text]) => {
    const button = el("button", { type: "button", textContent: text });
    button.setAttribute("aria-pressed", value === chosen);
    button.addEventListener("click", () => {
      chosen = value;
      if (current) current.lab = null;  // đổi lựa chọn thì quên lab cũ
      for (const other of $("picker").children) other.setAttribute("aria-pressed", other === button);
      $("question").focus();
    });
    return button;
  }));
});
