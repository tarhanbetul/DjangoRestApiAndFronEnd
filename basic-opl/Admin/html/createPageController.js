var app = angular.module("myApp", []);
app.controller('createPageController', ['$scope', '$http', function ($scope, $http) {

$scope.create=function(){
	document.getElementById("loader").style.display = "block";
	var settings = {
     "url": "http://127.0.0.1:8080/api/tutorials",
     "method": "POST",
     "timeout": 0,
	 "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({"name":$scope.ProductCreateData.name,"price":$scope.ProductCreateData.price,"amount":$scope.ProductCreateData.amount}),
};
$http(settings).then(function (response) {
	 document.getElementById("loader").style.display = "none";
     console.log(response);
     $scope.ProductCreateData = response.data;
	 window.location.replace("ProductList.html");
},
function(response){
	 document.getElementById("loader").style.display = "none";
	$scope.responseText ="An unexpected error has occurred. Data could not be created!!";
	 var x = document.getElementById("snackbar");
     x.className = "show";	 
     setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}
);
}
}]);