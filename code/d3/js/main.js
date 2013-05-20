jQuery(document).ready(function(){
	console.log("Document Ready");

	 	var margin = {top: 20, right: 20, bottom: 50, left: 80},
   			 width = 960 - margin.left - margin.right,
    		 height = 500 - margin.top - margin.bottom;


    	var x = d3.scale.ordinal()
   				 .rangeRoundBands([0, width], .1);

		var xAxis = d3.svg.axis()
				    .scale(x)
				    .orient("bottom");

    	var y = d3.scale.linear()
    			.range([height, 0]);

    	var yAxis = d3.svg.axis()
				    .scale(y)
				    .orient("left");

		var svg = d3.select("body").append("svg")
				    .attr("width", width + margin.left + margin.right)
				    .attr("height", height + margin.top + margin.bottom)
				  	.append("g")
				    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

		createviz("data/input2.csv");
	   jQuery("#select li").click(function(){
	   		console.log("Click Event");
	   		d3.selectAll("g.x.axis").remove();
	   		d3.selectAll("g.y.axis").remove();
	   		var te = $(this).text();
	   		var file="data/input2.csv";
	   		console.log(te);
	   		switch(te){
	   			case "Age 1 - 19":
	   				file="data/input1.csv";
	   				break;
	   			case "Age 20 - 50":
	   				file="data/input2.csv";
	   				break;
	   			case "Age 51 - 99":
	   				file="data/input3.csv";
	   				break;
	   			default:
	   				file="data/input1.csv";

	   		}
	   		createviz(file);

	   });

	   function createviz(file)
		{				
				d3.csv(file, function(error, data) {

					  console.log(data);
					  x.domain(data.map(function(d) { return d.age; }));
					  y.domain([0, d3.max(data, function(d) { return d.count; })]);
					  svg.append("g")
					      .attr("class", "x axis")
					      .attr("transform", "translate(0," + height + ")")
					      .call(xAxis)
					      .append("text")
					      .attr("x", 406)
					      .attr("dy", "2.5em")
					      .style("text-anchor", "end")
					      .text("Age");

					  	svg.append("g")
					      .attr("class", "y axis")
					      .call(yAxis)
					      .append("text")
					      .attr("transform", "rotate(-360)")
					      .attr("dy", ".5em")
					      .attr("x", "3.5em")
					      .style("text-anchor","end")
					      .text("No.of books Rated");

					   	var bars = svg.selectAll("rect")
					      .data(data)
					      .on("mouseover",function(d){
					      	showText(d.age,d.count)
					      });

					    bars
					      .enter().insert("rect")
					      .attr("class", "bar");

					      bars.transition().duration(1000)
					      .attr("x", function(d) { return x(d.age); })
					      .attr("width", x.rangeBand())
					      .attr("y", function(d) { return y(d.count); })
					      .attr("height", function(d) { return height - y(d.count); });
					      

					      bars.exit();		      

				});


		}

				function showText(age,count){
					console.log(age);

					var header =   jQuery('#helptext');  
						header.html(''); 
						header.append("Age:"+age+" <br> No.of Books Rated:"+count);
						console.log("header",header);

				}














});
       