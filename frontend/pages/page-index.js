import { webc } from 'marycat'
import css from './page-index.css'

export const pageIndex = webc({
  name: 'melior-page-index',
  props: {},
  css,
  fun: h => (h
    (header('.header')
      (div('.header-title')
        (span('🌠 Melior'))
      )
    )
    (div('.content')
      (section())
      (section())
      (section())
    )
  ),
})
