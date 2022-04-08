<script>
// readFile function is defined.
const fs = require('fs')
  
fs.readFile(FILE_LOCATION, function (err, data) {
  if (err) throw err; //change to dont throw error, change border coolor -> red
  if(data.includes('search string')){
   console.log(data) //keep green, do nothing
  }
});


</script>