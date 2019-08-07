import { webc } from 'marycat'
import css from './page-index.css'

export const pageIndex = webc({
  name: 'lecture-page-index',
  css,
  render: h => (h
    (div('.content')
      (section())
      (section())
      (section())
    )
  ),
})
