require 'serverspec'

describe 'Dockerfile' do

    # Tests
    #------

    it 'installs the right version of Ubuntu' do
        expect(get_os_version()).to include('Ubuntu 14.04')
    end


    # Functions
    #----------

    # Get os version of container
    def get_os_version
        command('lsb_release -a').stdout
    end
end

