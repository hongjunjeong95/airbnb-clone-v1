import gulp from "gulp";
import postCSS from "gulp-postcss";
import sass from "gulp-sass";
import minify from "gulp-csso";
import del from "del";
import tailwindcss from "tailwindcss";
import autoprefixer from "autoprefixer";

const css = () => {
  sass.compiler = require("node-sass");
  return gulp
    .src("assets/scss/styles.scss")
    .pipe(sass().on("error", sass.logError))
    .pipe(postCSS([tailwindcss, autoprefixer]))
    .pipe(minify())
    .pipe(gulp.dest("static/css"));
};

const clean = () => del(["static/css"]);

// exports.default = css;
export const dev = css;
