import React,{useState} from 'react'

const URL_API = "http://localhost:8080"

function App() {
	const [url,setUrl] = useState("")

	const [name,setName] = useState("")
	const [version,setVersion] = useState("")
	const [date,setDate] = useState("")
	const [download,setDownload] = useState("")
	const [description,setDescription] = useState("")
	const [logo,setLogo] = useState("")
	const [load,setLoad] = useState(false)

	const handleChange = function(event) {
		setUrl(event.target.value)
	}
	const handleUrl = function() {
		if(url) {
			setLoad(true)
			const input = {
				"url":url
			}
			fetch(URL_API,{
				method:"POST",
				headers: {
		    		'Accept': 'application/json',
		     		'Content-Type': 'application/json'
    			},
    			body:JSON.stringify(input)
			})
			.then(function (response) {
			    return response.json();
			}).then(function (result) {
				if(result) setLoad(false)
			    setName(result.data.name_application)
			    setVersion(result.data.version)
			    setDate(result.data.date_release)
			    setDownload(result.data.number_download)
			    setDescription(result.data.description)
			    setLogo(result.data.logo)
			}).catch (function (error) {
			    console.log('Request failed', error);
			})
		}
	}
  return (
    <div className="container-fluid">
    	<div className="row">
    		<div className="col-sm-4">
    			<div className="form-group">
				    <label htmlFor="url">Url</label>
				    <input type="text" className="form-control" onChange={handleChange} id="url" aria-describedby="url" placeholder="Enter url" />
  				</div>
  				<button className="btn btn-primary" onClick={handleUrl} style={{"borderRaduis":"5%","marginTop":"13px","padding":"3px 44px"}} type="submit">
  					Send
  				</button>
    		</div>
    		<div className="col-sm-8">
    			<div className="row">
    				<div className="col-sm-8" style={{"fontWeight":"bold"}}>
    					<div>Application name:<span style={{"color":"red"}}>{name}</span></div>
    					<div>Release date:<span style={{"color":"red"}}>{date}</span></div>
    					<div>Version:<span style={{"color":"red"}}>{version}</span></div>
    					<div>Download: <span style={{"color":"red"}}>{download}</span></div>
    					<div>Description: <span style={{"color":"red"}}>{description}</span></div>
    				</div>
    				<div className="col-sm-4">
    					<img src={logo} alt="logo" />
    				</div>
    			</div>
    			<div className="load" style={{"fontWeight":"bold","marginTop":"33px"}}>
					{load ? "Loading ...." : ""}
			</div>
    		</div>
    	</div>
    </div>
  );
}

export default App;
