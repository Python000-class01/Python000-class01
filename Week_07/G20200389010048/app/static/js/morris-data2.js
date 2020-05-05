$(function() {
    Morris.Bar({
        'element': 'morris-bar-chart',
        xkey: 'x',
        ykeys: ['y'],
        labels: ['采集评论数'],
        hideHover: 'auto',
        resize: true,
        data: [{
            x: '4-27',
            y: 100
        }, {
            x: '4-28',
            y: 75
        }]
    });
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "正面评论数",
            value: 12
        }, {
            label: "负面评论数",
            value: 30
        }],
        resize: rue
    });
});
