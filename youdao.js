const crypto=require('crypto')
const o = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl';
const n = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4';
function datas(t){
        const a = Buffer.alloc(16, crypto.createHash('md5').update(o).digest()),
        r = Buffer.alloc(16, crypto.createHash('md5').update(n).digest()),
        i = crypto.createDecipheriv("aes-128-cbc", a, r);
        let s = i.update(t, "base64", "utf-8");
        return s += i.final("utf-8"),
        s
}
text='密文'
console.log(datas(text))










