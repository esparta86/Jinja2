var myModule=angular.module('mymodule',[]);
myModule.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

myModule.controller('testController', ['$scope','$log',function($scope,$log){
	$scope.init = function()

      
	};


}]);