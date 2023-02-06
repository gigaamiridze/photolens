'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass')(require('sass'));

function buildStyles() {
  return gulp.src('static/scss/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('static/css'));
};

exports.buildStyles = buildStyles;
exports.watch = function () {
  gulp.watch('static/scss/**/*.scss', buildStyles);
};