import { State, webc, iter } from 'marycat'
import css from './toggle.css'

export const Toggle = webc('lecture-toggle', {
  css,
  props: {
    between: [],
  },
  init() {
    this.index = new State(0)
  },
  render(h, { between }) {
    const change = () => {
      this.index.v = (this.index.v + 1) % between.v.length
    }
    return h.click(change)
    (iter(between, (item, i) =>
      span(item.v).class(this.index.eq(i).tern('active', ''))
    ))
  },
  bind(state) {
    const { index, props } = this
    index.sub(i => state.v = props.between.v[i])
    return this
  },
})
