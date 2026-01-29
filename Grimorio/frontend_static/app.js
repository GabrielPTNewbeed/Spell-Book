// Grimório — frontend static app (localStorage)
const KEY = 'grimorio_magias_v1'

function uid(){return Date.now().toString(36)+Math.random().toString(36).slice(2,7)}

function load(){
  try{return JSON.parse(localStorage.getItem(KEY)||'[]')}
  catch(e){return []}
}
function save(arr){localStorage.setItem(KEY,JSON.stringify(arr))}

function getForm(){
  return {
    id: document.getElementById('spell-id').value || uid(),
    nome: document.getElementById('nome').value.trim(),
    escola: document.getElementById('escola').value.trim(),
    circulo: document.getElementById('circulo').value.trim(),
    acao: document.getElementById('acao').value.trim(),
    alcance: document.getElementById('alcance').value.trim(),
    concentracao: document.getElementById('concentracao').checked,
    preparada: document.getElementById('preparada').checked,
    descricao: document.getElementById('descricao').value.trim()
  }
}

function setForm(sp){
  document.getElementById('spell-id').value = sp.id || ''
  document.getElementById('nome').value = sp.nome || ''
  document.getElementById('escola').value = sp.escola || ''
  document.getElementById('circulo').value = sp.circulo || ''
  document.getElementById('acao').value = sp.acao || ''
  document.getElementById('alcance').value = sp.alcance || ''
  document.getElementById('concentracao').checked = !!sp.concentracao
  document.getElementById('preparada').checked = !!sp.preparada
  document.getElementById('descricao').value = sp.descricao || ''
}

function clearForm(){ setForm({}); document.getElementById('spell-id').value = '' }

function render(){
  const list = load()
  const container = document.getElementById('spell-list')
  container.innerHTML=''
  if(!list.length){ container.innerHTML='<li>Nenhuma magia cadastrada.</li>'; return }
  list.forEach(sp=>{
    const li=document.createElement('li'); li.className='spell-card'
    const left=document.createElement('div')
    left.innerHTML = `<strong>${escapeHtml(sp.nome)}</strong><div class="spell-meta">${escapeHtml(sp.escola||'')} · Círculo ${escapeHtml(sp.circulo||'')} · ${sp.acao||''} · Alcance: ${escapeHtml(sp.alcance||'')}</div><p>${escapeHtml(sp.descricao||'')}</p>`
    const actions=document.createElement('div'); actions.className='card-actions'
    const edit=document.createElement('button'); edit.className='small-btn'; edit.textContent='Editar'
    edit.onclick=()=>{ setForm(sp); window.scrollTo({top:0,behavior:'smooth'}) }
    const copy=document.createElement('button'); copy.className='small-btn'; copy.textContent='Copiar'
    copy.onclick=()=>{ navigator.clipboard.writeText(JSON.stringify(sp, null, 2)) }
    const del=document.createElement('button'); del.className='small-btn'; del.textContent='Excluir'
    del.onclick=()=>{ if(confirm('Excluir esta magia?')){ const remaining = load().filter(s=>s.id!==sp.id); save(remaining); render() } }
    actions.append(edit,copy,del)
    li.append(left,actions)
    container.appendChild(li)
  })
}

function escapeHtml(s){ if(!s) return ''; return s.replace(/[&<>\"]/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])) }

document.getElementById('spell-form').addEventListener('submit', e=>{
  e.preventDefault();
  const sp = getForm();
  if(!sp.nome){ alert('Nome é obrigatório'); return }
  const arr = load();
  const idx = arr.findIndex(x=>x.id===sp.id)
  if(idx>=0) arr[idx]=sp; else arr.unshift(sp)
  save(arr); clearForm(); render()
})

document.getElementById('clear-form').addEventListener('click', e=>{ e.preventDefault(); clearForm() })

document.getElementById('export-json').addEventListener('click', ()=>{
  const data = JSON.stringify(load(), null, 2)
  const blob = new Blob([data], {type:'application/json'})
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a'); a.href=url; a.download='magias.json'; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url)
})

document.getElementById('import-json').addEventListener('click', ()=>{
  const f = document.getElementById('import-file'); if(!f.files.length) { alert('Escolha um arquivo JSON primeiro'); return }
  const reader = new FileReader(); reader.onload = ()=>{
    try{
      const parsed = JSON.parse(reader.result)
      if(!Array.isArray(parsed)) throw new Error('Formato inválido')
      // assign ids if missing
      const normalized = parsed.map(p=>({ id: p.id||uid(), nome:p.nome||'', escola:p.escola||'', circulo:p.circulo||'', acao:p.acao||'', alcance:p.alcance||'', concentracao:!!p.concentracao, preparada:!!p.preparada, descricao:p.descricao||'' }))
      save(normalized)
      render()
    }catch(err){ alert('Erro ao importar: '+err.message) }
  }
  reader.readAsText(f.files[0])
})

document.getElementById('limpar-tudo').addEventListener('click', ()=>{ if(confirm('Apagar todas as magias?')){ save([]); render() } })

// Geração caótica: combina campos aleatoriamente entre magias existentes e presets
document.getElementById('gerar-caotica').addEventListener('click', ()=>{
  const pool = load();
  if(!pool.length){ alert('Precisa haver magias cadastradas para gerar variações caóticas'); return }
  const pick = (arr)=> arr[Math.floor(Math.random()*arr.length)]
  const nomeParts = [ 'Ruptura','Sombras','Fulgor','Sussurro','Tempestade','Vórtice','Lâmina','Coroa' ]
  const name = `${pick(nomeParts)} de ${pick(pool).escola || 'Mistério'} ${Math.floor(Math.random()*9)+1}`
  const nova = {
    id: uid(),
    nome: name,
    escola: pick(pool).escola || pick(nomeParts),
    circulo: pick(pool).circulo || (Math.floor(Math.random()*6)+1).toString(),
    acao: pick(pool).acao || '1 ação',
    alcance: pick(pool).alcance || 'toque',
    concentracao: Math.random() < 0.5,
    preparada: Math.random() < 0.5,
    descricao: `Magia caótica gerada automaticamente. Combina: ${pick(pool).nome} + ${pick(pool).nome}. Efeitos imprevisíveis.`
  }
  const arr = load(); arr.unshift(nova); save(arr); render(); setForm(nova); window.scrollTo({top:0,behavior:'smooth'})
})

// initial render
render()
