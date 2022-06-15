import cash from "cash-dom";
import {Chart, registerables} from "chart.js";
import 'chartjs-adapter-moment';


Chart.register(...registerables);
window.chartjs = Chart;


const Focus6 = ['#ffb91d', '#f97817', '#6de304', '#ff0000', '#732bea', '#c913ad']
window.colors = Focus6;

window.cash = cash;
