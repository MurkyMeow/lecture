import { attr, mount } from 'marycat'
import { div } from './bindings'

export function show(text: string, type: 'success' | 'error', timeout = 2000) {
  const vnode =
    div('.notification', text)
      (attr('data-type', type))
  const box = document.querySelector('.notification-box')
  if (!box) {
    return console.trace('Cant find a notification-box')
  }
  const [el] = mount(box, vnode)
  setTimeout(() => box.removeChild(el), timeout)
}
