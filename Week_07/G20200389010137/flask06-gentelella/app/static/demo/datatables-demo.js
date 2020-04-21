// Call the dataTables jQuery plugin
// $(document).ready(function() {
//   $('#dataTable').DataTable();
// });

$(document).ready(function() {
    $("#dataTable").DataTable({
        language: {
            "processing":   "处理中...",
            "lengthMenu":   "_MENU_ 记录/页",
            "zeroRecords":  "没有匹配的记录",
            "info":         "第 _START_ 至 _END_ 项记录，共 _TOTAL_ 项",
            "infoEmpty":    "第 0 至 0 项记录，共 0 项",
            "infoFiltered": "(由 _MAX_ 项记录过滤)",
            "infoPostFix":  "",
            "search":       "搜索:",
            "url":          "",
            "decimal":      ",",
            "thousands":    ".",
            "emptyTable":   "未找到符合条件的数据",
            "paginate": {
                "first":     "首页",
                "previous": "上页",
                "next":     "下页",
                "last":     "末页"
                }
            },
        retrieve: true,
        paging: true,
        ordering: false,
        info: true,
        autoWidth: false,
        pageLength: 10,//每页显示10条数据
        pagingType: "full_numbers", //分页样式：simple,simple_numbers,full,full_numbers，
        bFilter: false, //去掉搜索框方法
        bLengthChange: true,//也就是页面上确认是否可以进行选择一页展示多少条
        serverSide: true, //启用服务器端分页，要进行后端分页必须的环节
        ajax: function (data, callback, settings) {
            //封装相应的请求参数，这里获取页大小和当前页码
            var pagesize = data.length;//页面显示记录条数，在页面显示每页显示多少项的时候,页大小
            var start = data.start;//开始的记录序号
            var page = (data.start) / data.length + 1;//当前页码
            var data = {
                page: page,
                pagesize: pagesize,//这里只传了当前页和页大小，如果有其他参数，可继续封装
                }
            var json={
                dataArray:JSON.stringify(data)  // POST 提交的参数名为 dataArray，flask 中进行接收
                }
            $.ajax({
                type: "POST",
                url: "/douban",
                cache : false,          //禁用缓存
                data: json,             //传入已封装的参数
                dataType: "json",       //返回数据格式为json
                success: function(data) {
                    var arr = "";
                    if ('object' == typeof data) {
                        arr = data;
                    } else {
                        arr = $.parseJSON(data);//将json字符串转化为了一个Object对象
                    }
                    console.log("============数据==========")
                    console.log(arr)
                    var returnData = {};
                    //returnData.draw = arr.data.pagination.pageCount;//这里直接自行返回了draw计数器,应该由后台返回，没什么卵用！
                    returnData.recordsTotal = arr.data.pagination.totalCount;//totalCount指的是总记录数
                    returnData.recordsFiltered = arr.data.pagination.totalCount;//后台不实现过滤功能,全部的记录数都需输出到前端，记录数为总数
                    returnData.data = arr.data.douban;//返回汽车列表
                    console.log("======returnData.data=======")
                    console.log(returnData.recordsTotal)
                    console.log(returnData.recordsFiltered)
                    callback(returnData);//这个别忘了！！！
                    },
                error: function(XMLHttpRequest, textStatus, errorThrown) {
                    $.dialog.alert("查询失败");
                    $wrapper.spinModal(false);
                    }
                });
        },
        columns: [
            {"data": "id", "width": "50px", "defaultContent": "<i></i>"},
            {"data": "n_star", "width": "50px", "defaultContent": "<i></i>"},
            {"data": "short", "width": "120px", "defaultContent": "<i></i>"},
            {"data": "sentiment", "width": "80px", "defaultContent": "<i></i>"},
            ]
        })
    })
