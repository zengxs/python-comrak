use comrak::*;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyclass]
struct PyComrakOption {
    option: ComrakOptions,
}

#[pymethods]
impl PyComrakOption {
    #[new]
    fn new(obj: &PyRawObject) {
        obj.init(PyComrakOption {
            option: ComrakOptions::default(),
        });
    }

    fn enable(&mut self, ext: &str) -> PyResult<()> {
        match ext {
            "ext_gfm_table" => self.option.ext_table = true,
            "ext_autolink" => self.option.ext_autolink = true,
            "unsafe" => self.option.unsafe_ = true,
            _ => {
                return Err(pyo3::exceptions::ValueError::py_err(format!(
                    "Comrak: invalid extension name: \"{}\"",
                    ext
                )))
            }
        }
        Ok(())
    }
}

#[pyfunction]
fn py_markdown_to_html(md: &str, o: &PyComrakOption) -> PyResult<String> {
    Ok(markdown_to_html(md, &o.option))
}

#[pymodule]
fn _comrak(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(py_markdown_to_html))?;
    m.add_class::<PyComrakOption>()?;

    Ok(())
}
