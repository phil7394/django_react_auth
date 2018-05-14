import React, {Component} from 'react';
import {Button} from 'react-bootstrap';
import {API_URL} from './../constants';
import axios from 'axios';


class Details extends Component {

    componentWillMount() {

        this.setState({
            id: ""
        });
        const {userProfile, getProfile} = this.props.auth;
        if (!userProfile) {
            getProfile((err, profile) => {
                this.setState({id: this.getUserId(profile)});
            });
        } else {
            this.setState({id: this.getUserId(userProfile)});
        }
        this.getDetails.bind(this)

    }

    getUserId(profile) {
        return profile.sub.replace('auth0|', '');

    }

    getDetails() {
        const {getAccessToken} = this.props.auth;
        const headers = {'Authorization': `Bearer ${getAccessToken()}`};
        axios.get(`${API_URL}/api/${this.state.id}`, {headers})
            .then(response => this.setState({
                name: response.data.name,
                age: response.data.age,
                email: response.data.email,
                address: response.data.address,
                position: response.data.position,
                hireDate: response.data.hireDate,
                experience: response.data.experience
            }));

    }

    render() {
        console.log(this.state)
        const {isAuthenticated} = this.props.auth;
        const details = this.state;
        return (
            <div className="container">
                {
                    !isAuthenticated() &&
                    <p>Log in to get details from server.</p>
                }
                {
                    isAuthenticated() && (
                        <Button bsStyle="primary" onClick={this.getDetails.bind(this)}>
                            View your details
                        </Button>
                    )
                }
                {
                    this.state.email && (
                        <div className="container">
                            <div className="card bg-dark" style={{maxWidth: 40 + 'rem'}}>
                                <div className="card-header">
                                    <h1 className="text-white text-center">{details.name}</h1>
                                </div>
                                <ul className="list-group list-group-flush">
                                    <li className="list-group-item"><strong>Age:</strong> {details.age}</li>
                                    <li className="list-group-item"><strong>Email:</strong> {details.email}</li>
                                    <li className="list-group-item"><strong>Address:</strong> {details.address}</li>
                                    <li className="list-group-item"><strong>Position:</strong> {details.position}
                                    </li>
                                    <li className="list-group-item"><strong>Hire date:</strong> {details.hireDate}
                                    </li>
                                    <li className="list-group-item">
                                        <strong>Experience:</strong> {details.experience}
                                    </li>
                                </ul>
                            </div>

                        </div>
                    )
                }
            </div>
        );
    }
}

export default Details;
