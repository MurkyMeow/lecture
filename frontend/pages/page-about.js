import { webc } from 'marycat'

export const pageAbout = webc({
  name: 'lecture-page-about',
  props: {},
  fun: h => (h
    (div('About page!'))
  ),
})
