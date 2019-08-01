import { webc } from 'marycat'

export const pageAbout = webc({
  name: 'lecture-page-about',
  fun: h => (h
    (div('About page!'))
  ),
})
