const LABELS = { answer: "Trả lời", ask_back: "Hỏi lại", not_found: "Không có trong tài liệu", refuse: "Từ chối" };
const HAS_LAB = /(day|lab|ng[aà]y)\s*0*\d+/i;
let labs = [];
let chosen = "";  // "" = chưa chọn lab
let remembered = null;  // số lab máy chủ trả về từ câu trước; chỉ nhớ lab, không nhớ nội dung

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

function add(node) {
  $("welcome").hidden = true;
  $("messages").append(node);
  scrollDown();
  return node;
}

function fill(bubble, kind, label, text) {
  const badge = el("span", { className: "badge", textContent: label });
  badge.dataset.kind = kind;
  bubble.replaceChildren(badge, ...text.split("\n").filter((l) => l.trim()).map((l) => el("p", {}, ...inline(l))));
  scrollDown();
}

async function ask(raw) {
  // đã chọn lab mà câu hỏi không nêu lab thì gắn vào đầu, và hiện đúng câu đã gửi
  const question = chosen && !HAS_LAB.test(raw) ? `Lab ${chosen}: ${raw}` : raw;
  add(el("div", { className: "msg user", textContent: question }));
  const bubble = add(el("div", { className: "msg bot-msg" }, el("span", { className: "typing", textContent: "Đang tra tài liệu…" })));
  $("send").disabled = true;
  try {
    const response = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, lab: remembered }),
    });
    const data = await response.json();
    if (!response.ok) fill(bubble, "error", "Chưa trả lời được", data.error);
    else {
      remembered = data.lab;
      fill(bubble, data.decision || "", LABELS[data.decision] || "Kết quả", data.text);
    }
  } catch {
    fill(bubble, "error", "Chưa trả lời được", "Không kết nối được máy chủ.");
  } finally {
    $("send").disabled = false;
  }
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

$("clear").addEventListener("click", () => {
  for (const node of $("messages").querySelectorAll(".msg")) node.remove();
  remembered = null;
  $("welcome").hidden = false;
});

stats.then((data) => {
  labs = data.labs;
  const options = [["", "Chưa chọn lab"], ...labs.map((l) => [l.label, l.label])];
  $("picker").replaceChildren(...options.map(([value, text]) => {
    const button = el("button", { type: "button", textContent: text });
    button.setAttribute("aria-pressed", value === chosen);
    button.addEventListener("click", () => {
      chosen = value;
      remembered = null;  // đổi lựa chọn thì quên lab cũ
      for (const other of $("picker").children) other.setAttribute("aria-pressed", other === button);
      $("question").focus();
    });
    return button;
  }));
});
