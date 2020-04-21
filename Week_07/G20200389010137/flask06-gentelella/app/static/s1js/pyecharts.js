var barChart = echarts.init(document.getElementById('bar'), 'white', {renderer: 'canvas'});
var pieChart = echarts.init(document.getElementById('echart_pie'), 'white', {renderer: 'canvas'});
var wordCloudChart = echarts.init(document.getElementById('word_cloud'), 'white', {renderer: 'canvas'});

$(
    function () {
        barFetchData(barChart);
        setInterval(barFetchData, 29000);

        pieFetchData(pieChart);
        setInterval(pieFetchData, 31000);

        wordcloudFetchData(wordCloudChart);
        setInterval(wordcloudFetchData, 60000);
    }
);

function barFetchData() {
    $.ajax({
        type: "GET",
        url: "/barChart",
        dataType: 'json',
        success: function (result) {
            barChart.setOption(result);
        }
    });
}

function pieFetchData() {
    $.ajax({
        type: "GET",
        url: "/pieChart",
        dataType: 'json',
        success: function (result) {
            pieChart.setOption(result);
        }
    });
}

function wordcloudFetchData() {
    $.ajax({
        type: "GET",
        url: "/wordcloud",
        dataType: 'json',
        success: function (result) {
            wordCloudChart.setOption(result);
        }
    });
}