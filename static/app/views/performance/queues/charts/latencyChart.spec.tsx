import {OrganizationFixture} from 'sentry-fixture/organization';

import {render, screen, waitForElementToBeRemoved} from 'sentry-test/reactTestingLibrary';

import useOrganization from 'sentry/utils/useOrganization';
import {LatencyChart} from 'sentry/views/performance/queues/charts/latencyChart';

jest.mock('sentry/utils/useOrganization');

describe('latencyChart', () => {
  const organization = OrganizationFixture();
  jest.mocked(useOrganization).mockReturnValue(organization);

  let eventsStatsMock;

  beforeEach(() => {
    eventsStatsMock = MockApiClient.addMockResponse({
      url: `/organizations/${organization.slug}/events-stats/`,
      method: 'GET',
      body: {
        data: [],
      },
    });
  });
  it('renders', async () => {
    render(<LatencyChart />);
    screen.getByText('Avg Latency');
    expect(eventsStatsMock).toHaveBeenCalledWith(
      '/organizations/org-slug/events-stats/',
      expect.objectContaining({
        query: expect.objectContaining({
          yAxis: [
            'avg_if(span.self_time,span.op,queue.submit.celery)',
            'avg_if(span.self_time,span.op,queue.task.celery)',
            'count_op(queue.submit.celery)',
            'count_op(queue.task.celery)',
          ],
        }),
      })
    );
    await waitForElementToBeRemoved(() => screen.queryAllByTestId('loading-indicator'));
  });
});
