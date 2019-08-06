const box = document.body.querySelector('notification-box')

function show(text, type, timeout = 1000) {
  const el =
    div('.notification').class(type)
      (text)
  const $el = el(box)
  setTimeout(() => $el.remove(), timeout)
}

export default { show }
