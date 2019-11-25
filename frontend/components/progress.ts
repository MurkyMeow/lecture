import { customElement, PipeFn, defAttr, styleEl, style, cx } from 'marycat'
import { div } from '../bindings'
import css from './progress.css'

function viewProgress(h: PipeFn<ShadowRoot>, {
  max = defAttr(4),
  done = defAttr(0),
}) {
  return h
  (styleEl(css))
  (div(cx`bar-wrapper`)
    (div(cx`bar`)
      (style('--max', max.map(v => `${v}px`)))
      (style('--done', done.map(v => `${v}px`)))
    )
  )
}
export const Progress = customElement('lecture-progress', viewProgress)
