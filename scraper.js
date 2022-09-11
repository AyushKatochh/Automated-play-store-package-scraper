const puppeteer = require('puppeteer');

(async function scrape() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    //  const packageName = prompt("Enter package name");
    await page.goto(`https://play.google.com/store/apps/details?id=com.flipkart.shopsy`);
    await page.click('#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > c-wiz:nth-child(2) > div > section > header > div > div:nth-child(2) > button').then(() => console.log('clicked'));
         
    const versionElement = await page.$("[class='reAt0']");
    const publishedDate = await page.waitForSelector('#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div:nth-child(3) > div:nth-child(7) > div.reAt0')
    const publishedDateText = await (await publishedDate.getProperty('textContent')).jsonValue();
    const text = await (await versionElement.getProperty('textContent')).jsonValue();
   
    const selectedDetails = {
        version: text,
        publishedDateText: publishedDateText
    }
    console.log(selectedDetails);
    
  await browser.close()
})();
