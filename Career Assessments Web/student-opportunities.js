(function(){
  'use strict';
  const button=document.getElementById('listenPage'),status=document.getElementById('listenStatus');
  const supported='speechSynthesis' in window && 'SpeechSynthesisUtterance' in window;
  let reading=false;
  function reset(){reading=false;button.textContent='Listen to this page';button.setAttribute('aria-pressed','false');}
  button.addEventListener('click',()=>{
    if(!supported){status.textContent='Read aloud is not available in this browser. You can use your device’s reader or print this page.';return;}
    window.speechSynthesis.cancel();
    if(reading){reset();status.textContent='Reading stopped.';return;}
    const content=document.getElementById('main').cloneNode(true);
    content.querySelectorAll('.page-tools').forEach(el=>el.remove());
    const blocks=Array.from(content.querySelectorAll('h1,h2,h3,p,li')).map(el=>el.textContent.trim()).filter(Boolean);
    reading=true;button.textContent='Stop reading';button.setAttribute('aria-pressed','true');status.textContent='Reading this page.';
    function speak(i){
      if(!reading)return;
      if(i===blocks.length){reset();status.textContent='Reading finished.';return;}
      const utterance=new SpeechSynthesisUtterance(blocks[i]);utterance.lang='en-US';utterance.rate=.95;
      utterance.onend=()=>speak(i+1);
      utterance.onerror=()=>{reset();status.textContent='Reading stopped. Your browser’s voice may be unavailable.';};
      window.speechSynthesis.speak(utterance);
    }
    speak(0);
  });
  document.getElementById('printPage').addEventListener('click',()=>window.print());
  window.addEventListener('pagehide',()=>{if(supported)window.speechSynthesis.cancel();reset();});
})();
