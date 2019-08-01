import { webc, _if, State } from 'marycat'
import { Button } from './button'
import notification from '../notification'
import css from './form-auth.css'
import * as api from '../api'

export const FormAuth = webc({
  name: 'lecture-form-auth',
  css,
  props: {
    signup: true,
  },
  fun(h, { signup }) {
    const data = new State()
    const submit = async () => {
      const url = `/auth/${signup.v ? 'signup' : 'signin'}/`
      try {
        await api.post(url, data)
      } catch (err) {
        notification.show(err, 'error')
      }
    }
    return h
    (form().submit(submit).bind(data)
      (input('@email').type('email')
        .placeholder('Email')
        .required()
      )
      (input('@password').type('password')
        .placeholder('Пароль')
        .required()
      )
      (_if(signup)
        (input('@password_again').type('password')
          .placeholder('Повторите пароль')
          .required()
        )
      )
      (Button().text('Продолжить'))
    )
  },
})
