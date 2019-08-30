import { webc, _if, State } from 'marycat'
import { Button } from './button'
import { Toggle } from './toggle'
import css from './form-auth.css'
import * as api from '../api'

export const FormAuth = webc('lecture-form-auth', {
  css,
  props: {
    signup: true,
  },
  render(h) {
    const data = new State()
    const option = new State()
    const errors = new State({})
    const submit = async () => {
      const url = `/auth/${option.v === '👽' ? 'signup' : 'signin'}/`
      try {
        errors.v = {}
        await api.post(url, data.v)
      } catch (err) {
        if (err.status === 404) {
          errors._`main`.v = 'Неверный логин или пароль'
        } else if (err.status === 409) {
          const conflict = await err.json()
          if (conflict.email) errors._`email`.v = 'Email занят'
          if (conflict.name) errors._`name`.v = 'Никнейм занят'
        } else {
          errors._`main`.v = 'Не удаётся войти'
        }
      }
    }
    return h
    (form().bind(data)
      .prevent().submit(submit)
      (div('.error')(errors._`main`.or('')))
      (Toggle().between(['🔑', '👽'])
        .on('change', e => option.v = e.detail)
      )
      (input('@email').type('email')
        .placeholder('Email')
        .required()
        .validity(errors._`email`)
      )
      (input('@password').type('password')
        .placeholder('Пароль')
        .required()
      )
      (_if(option.eq('👽'))
        (input('@password_again').type('password')
          .placeholder('Повторите пароль')
          .required()
        )
        (input('@name')
          .placeholder('Никнейм')
          .required()
          .validity(errors._`name`)
        )
      )
      (button()
        (Button().text('Продолжить').click(submit))
      )
    )
  },
})
