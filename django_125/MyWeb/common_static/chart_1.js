/**
 * Created by Administrator on 2017/12/7.
 */

    var myChart = echarts.init(document.getElementById('main'));
    myChart.setOption({
        title:{
            text:'异步数据加载'
        },
        tooltip:{
            show:true,

        },

        xAxis:{
            type:'category',
            boundaryGap:false,
            data:[],
            splitLine: {
            show: false
            },
        },
        yAxis:{
            boundaryGap:[0,'100%'],
            type:'value',
            min:'dataMin',
            max:'dataMax',
            splitLine: {
            show: false
            },

        },
        series:[{
            name:'参数',
            type:'line',
            data:[]
        }]
    });
    myChart.showLoading();
    var date = [];
    var data = [];
    $.ajax({
        type:"get",
        // async:true,
        url:"test_data.json",
        data:{},
        dataType:"json",
        success:function(result){
            var datas=result
            if(result){

                var m=0;
                for(var i=0;i<result.length;i++){
                    if(m<1000){
                        datas.shift();
                        date.push(result[i]["time"]);
                        data.push(result[i]["AM23SIG0206.AV"]);
                        m+=1;
                    }
                    else{
                        break;

                    }
                myChart.hideLoading();
                setInterval(function(){
                    for(var n=0;n<2;n++){

                        date.shift();
                        date.push(datas[n]["time"]);
                        data.shift();
                        data.push(datas[n]["AM23SIG0206.AV"]);
                    }
                    myChart.setOption({
                    xAxis:{
                        data:date
                    },
                    series:[
                        {
                            name:"参数",
                            data:data
                        }
                    ]});
                    for(var nn=0;nn<2;nn++){
                        datas.shift()
                    }

                },2000);

                }
            }
        },
        error:function(errorMsg){
            alert("图表请求数据失败！");
            myChart.hideLoading();
        }
    })
