function show(text, type, timeout = 2000) {
  const el =
    div('.notification').attr('data-type', type)
      (text)
  const $el = el.connect(
    document.querySelector('.notification-box')
  )
  setTimeout(() => $el.remove(), timeout)
}

export default { show }
