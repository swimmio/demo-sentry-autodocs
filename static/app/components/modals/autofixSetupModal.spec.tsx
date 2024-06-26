import {act, renderGlobalModal, screen, userEvent} from 'sentry-test/reactTestingLibrary';

import {openModal} from 'sentry/actionCreators/modal';
import {AutofixSetupModal} from 'sentry/components/modals/autofixSetupModal';

describe('AutofixSetupModal', function () {
  it('renders the integration setup instructions', async function () {
    MockApiClient.addMockResponse({
      url: '/issues/1/autofix/setup/',
      body: {
        genAIConsent: {ok: true},
        integration: {ok: false},
      },
    });

    const closeModal = jest.fn();

    renderGlobalModal();

    act(() => {
      openModal(modalProps => <AutofixSetupModal {...modalProps} groupId="1" />, {
        onClose: closeModal,
      });
    });

    expect(await screen.findByText('Install the GitHub Integration')).toBeInTheDocument();
    expect(
      screen.getByText(/Install the GitHub integration by navigating to/)
    ).toBeInTheDocument();
  });

  it('displays successful integration text when it is installed', async function () {
    MockApiClient.addMockResponse({
      url: '/issues/1/autofix/setup/',
      body: {
        genAIConsent: {ok: false},
        integration: {ok: true},
      },
    });

    const closeModal = jest.fn();

    renderGlobalModal();

    act(() => {
      openModal(modalProps => <AutofixSetupModal {...modalProps} groupId="1" />, {
        onClose: closeModal,
      });
    });

    expect(
      await screen.findByText(/The GitHub integration is already installed/)
    ).toBeInTheDocument();
  });

  it('shows success text when steps are done', async function () {
    MockApiClient.addMockResponse({
      url: '/issues/1/autofix/setup/',
      body: {
        genAIConsent: {ok: true},
        integration: {ok: true},
      },
    });

    const closeModal = jest.fn();

    renderGlobalModal();

    act(() => {
      openModal(modalProps => <AutofixSetupModal {...modalProps} groupId="1" />, {
        onClose: closeModal,
      });
    });

    expect(
      await screen.findByText("You've successfully configured Autofix!")
    ).toBeInTheDocument();

    await userEvent.click(screen.getByRole('button', {name: "Let's go"}));

    expect(closeModal).toHaveBeenCalled();
  });
});
