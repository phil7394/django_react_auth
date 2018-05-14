import React, {Component} from 'react';
import {Panel, ControlLabel, Glyphicon} from 'react-bootstrap';
import './Profile.css';

class Profile extends Component {
    componentWillMount() {
        this.setState({profile: {}});
        const {userProfile, getProfile} = this.props.auth;
        if (!userProfile) {
            getProfile((err, profile) => {
                this.setState({profile});
            });
        } else {
            this.setState({profile: userProfile});
        }
    }

    render() {
        const {profile} = this.state;
        return (
            <div className="container" style={{maxWidth: 70 + 'rem'}}>
                <div className="bg-dark">
                    <Panel header="Profile">
                        <img src={profile.picture} alt="profile" style={{maxWidth: 15 + 'rem', maxHeight: 15 + 'rem'}}/>
                        <div>
                            <ControlLabel><Glyphicon glyph="user"/> Nickname</ControlLabel>
                            <h3>{profile.nickname}</h3>
                        </div>
                        <pre>{JSON.stringify(profile, null, 2)}</pre>
                    </Panel>
                </div>
            </div>
        );
    }
}

export default Profile;
