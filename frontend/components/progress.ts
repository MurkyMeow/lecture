import { customElement, PipeFn, defAttr, styleEl, repeat, on, attr, dispatch } from 'marycat'
import { span } from '../bindings'
import css from './progress.css'

function viewProgress(h: PipeFn<ShadowRoot>, {
  max = defAttr(4),
  active = defAttr(-1),
  done = defAttr<number[]>([]),
}) {
  const items = max.map(v => [...Array(v).keys()])
    return h
    (styleEl()(css))
    (repeat(items, x => x.toString(), (_, i) =>
      (span()
        (on('click', () => h(dispatch('change', i.v))))
        (attr('data-done', done.map(v => v.includes(i.v))))
        (attr('data-active', active.eq(i)))
      )
    ))
}
export const Progress = customElement('lecture-progress', viewProgress)
