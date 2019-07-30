import { webc } from 'marycat'
import css from './page-index.css'

export const pageIndex = webc({
  name: 'lecture-page-index',
  props: {},
  css,
  fun: h => (h
    (header('.header')
      (div('.header-title')
        (span('🌌 lecture'))
      )
    )
    (div('.content')
      (section())
      (section())
      (section())
    )
  ),
})
