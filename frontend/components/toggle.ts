import { customElement, PipeFn, defAttr, styleEl, on, repeat, attr, TypedDispatch } from 'marycat'
import { span } from '../bindings'
import css from './toggle.css'

type ToggleDispatch =
  TypedDispatch<{ change: string }>

function viewToggle(h: PipeFn<ShadowRoot>, {
  tabs = defAttr<string[]>([]),
  current = defAttr(0),
}, t_dispatch: ToggleDispatch) {
  return h
  (on('click', () => {
    current.v = (current.v + 1) % tabs.v.length
    h(t_dispatch('change', tabs.v[current.v]))
  }))
  (styleEl()(css))
  (repeat(tabs, x => x, (item, i) =>
    (span(item.v)
      (attr('class', current.eq(i).and('active')))
    )
  ))
}
export const Toggle = customElement('lecture-toggle', viewToggle)
