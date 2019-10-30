import { customElement, styleEl, PipeFn } from 'marycat'
import { button, slot } from '../bindings'
import css from './button.css'

function viewButton(h: PipeFn<ShadowRoot>) {
  return h
  (styleEl()(css))
  (button()(slot()))
}
export const Button = customElement('lecture-button', viewButton)
