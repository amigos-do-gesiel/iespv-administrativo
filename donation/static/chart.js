google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

var a = {{data_json|safe}}

function drawChart() {
	
	var data = google.visualization.arrayToDataTable([

		['Data', 'Valor Doação'],
		['2013',  1000],
		['2014',  1170],
		['2015',  660],
		['2016',  1030]

	]);


	var options = {
		title: 'Company Performance',
		hAxis: {title: 'Year',  titleTextStyle: {color: '#333'}},
		vAxis: {minValue: 0}
	};

	var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
	chart.draw(data, options);
}
