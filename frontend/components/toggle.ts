import { State, customElement, PipeFn, defAttr, styleEl, on, dispatch, repeat, attr } from 'marycat'
import { span } from '../bindings'
import css from './toggle.css'

function viewToggle(h: PipeFn, {
  tabs = defAttr<string[]>([]),
}) {
  const index = new State(0)
  return h
  (on('click', () => {
    index.v = (index.v + 1) % tabs.v.length
    h(dispatch('change', tabs.v[index.v]))
  }))
  (styleEl()(css))
  (repeat(tabs, x => x, (item, i) =>
    (span(item.v)
      (attr('class', index.eq(i).and('active')))
    )
  ))
}
export const Toggle = customElement('lecture-toggle', viewToggle)
