function echarts_line(chartid, labelname, legends, labels, datas){
        let myChart = echarts.init(document.getElementById(chartid));
        myChart.setOption({
            title : {
                text:labelname,
                x:'center',
                textStyle:{
                    color: 'red',
                    fontSize: 20
                }
            },
            legend: {
                    bottom: 0,
                    data:legends
                            },
            tooltip: {
                trigger: 'axis'
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
            xAxis: {
                type: 'category',
                name: '时间',
                data: labels,
            },
            yAxis: {
                type: 'value',
                name: '利用率(单位%)',
                axisLabel: {
                            formatter: '{value} %' // 格式化,单位为%
                            },
                min: 0,
                max: 100
            },
            series: datas
        })
    }


function echarts_bar(chartid, labelname, labels, datas, color){
        let myChart = echarts.init(document.getElementById(chartid));

        myChart.setOption({
            title : {
                text:labelname,
                // subtext:"bar",
                x:'center',
                textStyle:{
                    color: 'red',
                    fontSize: 20
                }
            },
            tooltip: {
                trigger: 'axis'
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
                    xAxis: {
                type: 'category',
                name: '时间',
                data: labels
            },
            yAxis: {
                type: 'value',
                name: '利用率'
            },
            series: [{
                name: 'Line 1',
                data: datas,
                smooth:true,
                type: 'bar',
                lineStyle: {color: color}
            }]
        })
    }


function echarts_pie(chartid, labelname, labels, datas){
        let myChart = echarts.init(document.getElementById(chartid));

        myChart.setOption({
            title : {
                text:labelname, // 主标题
                x:'center', // 主标题位置
                textStyle:{
                    color: 'red', // 颜色
                    fontSize: 20 //字体大小
                }
            },
            toolbox: {
                feature: {
                    saveAsImage: {} //允许保存为图片
                }
            },
            // 鼠标移动上去的提示
            tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                },
            // 左上角的提示
            legend: {
                orient: 'vertical',
                x: 'left',
                data: labels
            },
            series: [
                {
                    name:'报名方向', // 本圈的大标题
                    type:'pie', // 饼状图
                    radius: ['50%', '70%'], //小圈 和 大圈的大小
                    avoidLabelOverlap: false,
                    label: {
                        //是否显示名字在侧面
                        normal: {
                            show: false,
                            position: 'center'
                        },
                        // 是否在饼中间显示名字
                        emphasis: {
                            show: true,
                            textStyle: {
                                fontSize: '30',
                                fontWeight: 'bold'
                            }
                        }
                    },
                    // 是否显示连接饼到名字的线
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data: datas
                }
            ]
    })}
