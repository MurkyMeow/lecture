import { webc } from 'marycat'

export const pageAbout = webc('lecture-page-about', {
  render: h => (h
    (div('About page!'))
  ),
})
