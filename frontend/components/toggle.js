import { State, webc, iter } from 'marycat'
import css from './toggle.css'

export const Toggle = webc('lecture-toggle', {
  css,
  props: {
    between: [],
  },
  render(h, { between }) {
    const index = new State(0)
    return h
    .click(() => {
      index.v = (index.v + 1) % between.v.length
      h.emit('change', between.v[index.v])
    })
    (iter(between, (item, i) =>
      span(item.v).class(index.eq(i).tern('active', ''))
    ))
  },
})
