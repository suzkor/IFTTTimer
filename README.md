# IFTTTimer
IFTTTで時間差動作したかったので（3時間後にエアコンOFFとか）  

叩きたいAPIとURLと、何分後かをのっけてPOSTするとその時間にそのURLを叩いてくれる  
URLと時間をのっけてDynamoDBに突っ込み、1分ごとに動作するmainがそれを拾ってくる感じ