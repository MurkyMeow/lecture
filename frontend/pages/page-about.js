import { webc } from 'marycat'

export const pageAbout = webc({
  name: 'melior-page-about',
  props: {},
  fun: h => (h
    (div('About page!'))
  ),
})
