
import { readFile } from 'fs';
// readFile function is defined  

readFile(test.txt, function (err, data){
  
  if (data.includes('test123454'))
    document.getElementById("Tommy").style.border = "15px solid green"     //change border color - red

  else
    document.getElementById("Tommy").style.border = "15px solid red"     //change border color - red

})


//HAS TO BE RUN FROM A SERVER. CAN'T BE RUN FROM FILE://C:/BOT.HTML

//on bash..
// npm install -g live-server // Install globally via npm
// live-serverlive-server