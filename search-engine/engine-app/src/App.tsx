import { useState } from 'react'
import { advancedSearchMutation, searchMutation } from './api';
import './App.css'

type Input = 'simple' | 'marca' | 'memoria' | 'armazenamento';

interface FormInputs {
  simple?: string;
  marca?: string;
  memoria?: string;
  armazenamento?: string;
}

function App() {
  const [links, setLinks] = useState([])
  const [advancedQuerySelected, setAdvancedQuerySelected] = useState(false)
  const [formInputsValues, setFormInputsValues] = useState<FormInputs>({} as FormInputs);

  const handleChangeToAdvancedQueryClick = () => {
    setAdvancedQuerySelected(!advancedQuerySelected)
    setLinks([])
  }

  const handleSearchInputOnChange = (input: Input, value: string) => {
    setFormInputsValues({ ...formInputsValues, [input]: value });
  }

  const handleSearchClick = async () => {
    const { simple } = formInputsValues;
    if (simple) {
      const results = await searchMutation(simple)
      console.log(results)
      setLinks(results)
    }
  }

  const handleAdvancedSearchClick = async () => {
    const { marca, memoria, armazenamento } = formInputsValues;
    if (marca && memoria && armazenamento) {
      const results = await advancedSearchMutation(marca, memoria, armazenamento)
      setLinks(results)
    }
  }

  return (
    <div className="container">
      {!advancedQuerySelected && (
        <div className="form-container">
          <span>🧐</span>
          <input type="text"
            className="search-input"
            placeholder="Descreva as características do que procuras..."
            onChange={(e) => handleSearchInputOnChange('simple', e.currentTarget.value)}
          />
          <div className="form-button-container">
            <button onClick={handleSearchClick}>Ache meu smartphone</button>
            <button onClick={handleChangeToAdvancedQueryClick}>
              Pesquisa avançada
            </button>
          </div>
          <div className='links-container'>
            {links.length > 0 &&
              links.map(link => (
              <a href={link} target="_blank">{link}<br/></a>
              ))
            }
          </div>
        </div>
      )}

      {advancedQuerySelected && (
        <div className="form-container">
          <span>🕵🏻‍♂️</span>
          <input
            type="text"
            className="search-input"
            placeholder="Marca / Modelo"
            onChange={(e) => handleSearchInputOnChange('marca', e.currentTarget.value)}
          />
          <input
            type="text"
            className="search-input"
            placeholder="Memória"
            onChange={(e) => handleSearchInputOnChange('memoria', e.currentTarget.value)}
          />
          <input
            type="text"
            className="search-input"
            placeholder="Armazenamento"
            onChange={(e) => handleSearchInputOnChange('armazenamento', e.currentTarget.value)}
          />
          <div className="form-button-container">
            <button onClick={handleAdvancedSearchClick}>Ache meu smartphone</button>
            <button onClick={handleChangeToAdvancedQueryClick}>
              Pesquisa simples
            </button>
          </div>
          <div className='links-container'>
            {links.length > 0 &&
              links.map(link => (
              <a href={link} target="_blank">{link}<br/></a>
              ))
            }
          </div>
        </div>
      )}

    </div>
  )
}

export default App
