// Chữ của model chỉ được đưa vào trang bằng textContent / createTextNode, không dùng innerHTML.
const $ = (id) => document.getElementById(id);
const el = (tag, props = {}, ...children) => {
  const node = Object.assign(document.createElement(tag), props);
  node.append(...children);
  return node;
};

// Số liệu chung của hai trang; sidebar được điền ngay khi tải xong.
const stats = fetch("/api/stats").then(async (response) => {
  const data = await response.json();
  if (!response.ok) throw new Error(data.error);
  $("model").textContent = data.model ? "Model: " + data.model : "Chế độ giả, chưa gọi model";
  $("labs").replaceChildren(...data.labs.map((lab) =>
    el("li", {}, el("a", { href: lab.url, target: "_blank", rel: "noopener noreferrer" },
      el("span", { textContent: lab.label }), el("small", { textContent: lab.files + " file" })))));
  return data;
});
stats.catch((error) => { $("model").textContent = error.message || "Không tải được số liệu"; });
