$(function() {
    pos_obj = document.getElementById("positive");
    neg_obj = document.getElementById("negative");
    pos = "50";
    neg = "50";
    if (pos_obj) {
        pos = pos_obj.value;
    }

    if (neg_obj) {
        neg = neg_obj.value;
    }

    Morris.Donut({
        element: 'morris-sentiment-chart',
        data: [{
            label: "正向情感评论数量",
            value: parseInt(pos)
        }, {
            label: "负向情感评论数量",
            value: parseInt(neg)
        }],
        resize: true
    });


    cnt_obj0 = document.getElementById("cnt0");
    cnt_obj1 = document.getElementById("cnt1");
    cnt_obj2 = document.getElementById("cnt2");
    cnt_obj3 = document.getElementById("cnt3");
    cnt_obj4 = document.getElementById("cnt4");
    cnt_obj5 = document.getElementById("cnt5");

    cnt0 = 0;
    cnt1 = 0;
    cnt2 = 0;
    cnt3 = 0;
    cnt4 = 0;
    cnt5 = 0;
    if (cnt_obj0 && cnt_obj1 && cnt_obj2 && cnt_obj3 && cnt_obj4 && cnt_obj5) {
        cnt0 = parseInt(cnt_obj0.value);
        cnt1 = parseInt(cnt_obj1.value);
        cnt2 = parseInt(cnt_obj2.value);
        cnt3 = parseInt(cnt_obj3.value);
        cnt4 = parseInt(cnt_obj4.value);
        cnt5 = parseInt(cnt_obj5.value);
    }

    neg_obj = document.getElementById("negative");
    pos = "50";
    neg = "50";
    if (pos_obj) {
        pos = pos_obj.value;
    }

    if (neg_obj) {
        neg = neg_obj.value;
    }


    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: '前10分钟',
            a: cnt0,
        }, {
            y: '前20分钟至10分钟',
            a: cnt1,
        }, {
            y: '前30分钟至20分钟',
            a: cnt2,
        }, {
            y: '前40分钟至30分钟',
            a: cnt3,
        }, {
            y: '前50分钟至40分钟',
            a: cnt4,
        }, {
            y: '前60分钟至50分钟',
            a: cnt5,
        } ],
        xkey: 'y',
        ykeys: ['a'],
        labels: ['Series A'],
        hideHover: 'auto',
        resize: true
    });


    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '2010 Q1',
            iphone: 2666,
            ipad: null,
            itouch: 2647
        }, {
            period: '2010 Q2',
            iphone: 2778,
            ipad: 2294,
            itouch: 2441
        }, {
            period: '2010 Q3',
            iphone: 4912,
            ipad: 1969,
            itouch: 2501
        }, {
            period: '2010 Q4',
            iphone: 3767,
            ipad: 3597,
            itouch: 5689
        }, {
            period: '2011 Q1',
            iphone: 6810,
            ipad: 1914,
            itouch: 2293
        }, {
            period: '2011 Q2',
            iphone: 5670,
            ipad: 4293,
            itouch: 1881
        }, {
            period: '2011 Q3',
            iphone: 4820,
            ipad: 3795,
            itouch: 1588
        }, {
            period: '2011 Q4',
            iphone: 15073,
            ipad: 5967,
            itouch: 5175
        }, {
            period: '2012 Q1',
            iphone: 10687,
            ipad: 4460,
            itouch: 2028
        }, {
            period: '2012 Q2',
            iphone: 8432,
            ipad: 5713,
            itouch: 1791
        }],
        xkey: 'period',
        ykeys: ['iphone', 'ipad', 'itouch'],
        labels: ['iPhone', 'iPad', 'iPod Touch'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });
});
