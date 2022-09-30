const puppeteer = require('puppeteer');
const mongoose = require("mongoose");
require("dotenv").config();
const mongoURI = process.env.mongoURI;




async function scrape() {
    mongoose.connect("Your_URI", {useNewUrlParser: true});

    const PackageSchema = new mongoose.Schema({
    version: String,
    updatedDateText: String

})

const PSchema = new mongoose.model("PSchema", PackageSchema);

    const browser = await puppeteer.launch({ headless: false });
       const page = await browser.newPage();
            const readline = require("readline");
            const rl = readline.createInterface({
                input: process.stdin,
                output: process.stdout
            });

            let fulfill;
            const answerPromise = new Promise(x => fulfill = x);
            rl.question('Enter the Package Name: ', (answer) => {
             fulfill(answer);
             rl.close();
             });  

            const PackageName = await answerPromise;
            let dataObj = {};

          
            await page.goto(`https://play.google.com/store/apps/details?id=${PackageName}`);   

            

            await page.click('#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > c-wiz:nth-child(2) > div > section > header > div > div:nth-child(2) > button').then(() => console.log('clicked'));


        const versionElement = await page.waitForSelector('#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div:nth-child(3) > div:nth-child(1) > div.reAt0')
        const updatedDate = await page.waitForSelector('#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div:nth-child(3) > div:nth-child(2) > div.reAt0')
        const updatedDateText = await (await updatedDate.getProperty('textContent')).jsonValue();
        const text = await (await versionElement.getProperty('textContent')).jsonValue();

      
          const selectedDetails = {
            version: text,
            updatedDateText: updatedDateText
        }
          
          dataObj = {
                version: selectedDetails.version,
                updatedDateText: selectedDetails.updatedDateText
            }
          
           
             console.log(dataObj);
          

          
             
           let collectedData =new PSchema({
             version: dataObj.version,
             updatedDateText: dataObj.updatedDateText
           });

          
              
           
          
            await collectedData.save().then(console.log("Data Entered Successfully"))
           



           console.log(collectedData);

           

         
            let previousPackageDate = collectedData.updatedDateText;
            if(updatedDateText != previousPackageDate) {
              console.log(`Previous package date: ${previousPackageDate}`);
            } else {
              console.log(`updatedDateText ${updatedDateText}`);
            }
            
          
    
        
      
            
  await browser.close();
  return dataObj;

   
}
scrape();
    
module.exports = scrape;
 

