import { chromium } from 'playwright';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage();
await p.goto('file://' + process.cwd() + '/primavera.html', { waitUntil: 'load' });
await p.waitForTimeout(700);
await p.pdf({ path: 'Mais-cuidados-para-a-primavera.pdf', format: 'A4',
              printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
// prévia visual das duas primeiras páginas
await p.setViewportSize({ width: 794, height: 1123 });
await p.screenshot({ path: 'previa-capa.jpg', type: 'jpeg', quality: 84,
                     clip: { x: 0, y: 0, width: 794, height: 1123 } });
await b.close();
console.log('gerado');
