import { customElement, styleEl, PipeFn, defAttr, attr } from 'marycat'
import { button, slot } from '../bindings'
import css from './button.css'

function viewButton(h: PipeFn<ShadowRoot>, {
  color = defAttr<'green' | 'red'>('green'),
}) {
  return h
  (styleEl()(css))
  (attr('color', color))
  (button()(slot()))
}
export const Button = customElement('lecture-button', viewButton)
