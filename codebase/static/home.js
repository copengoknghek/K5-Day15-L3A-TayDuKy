const TYPES = { thuong: "Thường", kho: "Khó", tu_choi: "Cần từ chối" };

// Đã chấm đủ thì hiện số câu đạt; chưa chấm thì chỉ hiện số câu đúng nhánh và ghi rõ.
function drawEval(run) {
  if (!run) {
    $("bars").textContent = "Chưa có lượt đánh giá nào.";
    return;
  }
  const graded = run.passed !== null;
  const key = graded ? "passed" : "right";
  const good = graded ? "Đạt" : "Đúng nhánh";
  const bad = graded ? "Chưa đạt" : "Lệch nhánh";
  $("bars-title").textContent = `Lượt ${run.run}: ${good.toLowerCase()} theo loại câu`;
  $("legend-right").textContent = good;
  $("legend-wrong").textContent = bad;

  const types = Object.entries(run.types);
  const max = Math.max(...types.map(([, t]) => t.total));
  $("bars").replaceChildren(...types.map(([name, t]) => {
    const label = TYPES[name] || name;
    const stack = el("div", { className: "stack",
      title: `${label}: ${t[key]} ${good.toLowerCase()}, ${t.total - t[key]} ${bad.toLowerCase()}` });
    for (const [kind, count] of [["wrong", t.total - t[key]], ["right", t[key]]]) {
      if (!count) continue;
      const part = el("span", { className: kind });
      part.style.height = (count / max) * 100 + "%";
      stack.append(part);
    }
    return el("div", { className: "bar" }, stack,
      el("b", { textContent: `${t[key]}/${t.total}` }), el("small", { textContent: label }));
  }));

  const count = graded ? run.passed : run.right;
  const share = count / run.total;
  const percent = Math.round(share * 100);
  $("ring-title").textContent = `Lượt ${run.run}: tỉ lệ ${good.toLowerCase()}`;
  $("ring-sub").textContent = `${good} so với ${bad.toLowerCase()}, ${run.total} câu thử`;
  $("percent").textContent = percent + "%";
  drawPie(share);
  $("pie").setAttribute("aria-label", `${good} ${count} trên ${run.total} câu`);

  // mũi tên chỉ hiện khi có lượt trước đã chấm để so, không thì chỉ ghi số câu
  const previous = graded && run.previous !== null ? run.previous : null;
  $("pie-legend").replaceChildren(...[["good", good, count, previous], ["rest", bad, run.total - count,
    previous === null ? null : run.total - previous]].map(([kind, label, now, before]) => {
    const delta = el("small", { textContent: `${now} câu` });
    if (before !== null && now !== before) {
      const better = kind === "good" ? now > before : now < before;
      delta.className = better ? "up" : "down";
      delta.textContent = `${now} câu ${now > before ? "▲" : "▼"} ${Math.abs(now - before)}`;
    }
    return el("li", { className: kind }, el("i"), el("span", { textContent: label }), delta);
  }));

  let note = "";
  if (!graded) note = "Chưa chấm xong.";
  else if (share < 0.8) note = "Chưa đạt chuẩn của nhóm (cần từ 80%).";
  else note = "Chuẩn còn xét thêm ngưỡng từng metric.";
  $("ring-note").textContent = note;
}

// Bánh tròn có lỗ; phần "đạt" tách nhẹ ra ngoài.
function drawPie(share) {
  const svg = "http://www.w3.org/2000/svg";
  const point = (r, turn) => `${(r * Math.sin(turn * 2 * Math.PI)).toFixed(2)} ${(-r * Math.cos(turn * 2 * Math.PI)).toFixed(2)}`;
  const slice = (kind, from, to, offset) => {
    const path = document.createElementNS(svg, "path");
    const large = to - from > 0.5 ? 1 : 0;
    path.setAttribute("class", kind);
    path.setAttribute("d", `M ${point(52, from)} A 52 52 0 ${large} 1 ${point(52, to)} L ${point(19, to)} A 19 19 0 ${large} 0 ${point(19, from)} Z`);
    const middle = (from + to) / 2 * 2 * Math.PI;
    path.setAttribute("transform", `translate(${offset * Math.sin(middle)} ${-offset * Math.cos(middle)})`);
    path.setAttribute("stroke", "#fff");
    path.setAttribute("stroke-width", "1.5");
    return path;
  };
  // 0% hoặc 100% thì vẽ gần trọn vòng (một cung 360 độ không vẽ được)
  const cut = Math.min(Math.max(share, 0.0001), 0.9999);
  $("pie").replaceChildren(slice("rest", cut, 1, 0), slice("good", 0, cut, 5));
}

stats.then((data) => {
  $("n-labs").textContent = data.labs.length;
  $("n-files").textContent = data.files;
  $("n-sections").textContent = data.sections;
  drawEval(data.eval);
});
