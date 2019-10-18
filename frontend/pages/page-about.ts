import { customElement, PipeFn } from 'marycat'
import { div } from '../bindings'

function viewAbout(h: PipeFn) {
  return h
  (div('About page!'))
}
export const pageAbout = customElement('lecture-page-about', viewAbout)
